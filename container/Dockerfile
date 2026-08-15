FROM node:18-alpine AS builder
WORKDIR /cv
RUN apk add git

# ADD https://github.com/mrozekma/cv.git /cv
COPY . .

RUN yarn install && yarn build

# texmf-dist-fontsextra is ~1.9GB but we only need 3 of the font families it bundles
# (~25MB), so install it in a throwaway stage and cherry-pick just those out of it.
FROM nginx:alpine AS fonts
RUN apk add --no-cache texmf-dist-fontsextra

FROM nginx:alpine
RUN apk add bash fcgiwrap poetry supervisor uv \
	texlive texlive-xetex \
	texmf-dist-latex texmf-dist-latexrecommended texmf-dist-latexextra \
	texmf-dist-pictures
COPY --from=fonts /usr/share/texmf-dist/tex/latex/fontawesome5 /usr/share/texmf-dist/tex/latex/fontawesome5
COPY --from=fonts /usr/share/texmf-dist/tex/latex/roboto /usr/share/texmf-dist/tex/latex/roboto
COPY --from=fonts /usr/share/texmf-dist/tex/latex/sourcesanspro /usr/share/texmf-dist/tex/latex/sourcesanspro
COPY --from=fonts /usr/share/texmf-dist/fonts/opentype/public/fontawesome5 /usr/share/texmf-dist/fonts/opentype/public/fontawesome5
COPY --from=fonts /usr/share/texmf-dist/fonts/opentype/adobe/sourcesanspro /usr/share/texmf-dist/fonts/opentype/adobe/sourcesanspro
COPY --from=fonts /usr/share/texmf-dist/fonts/opentype/google/roboto /usr/share/texmf-dist/fonts/opentype/google/roboto
COPY --from=fonts /usr/share/texmf-dist/fonts/enc/dvips/fontawesome5 /usr/share/texmf-dist/fonts/enc/dvips/fontawesome5
COPY --from=fonts /usr/share/texmf-dist/fonts/enc/dvips/roboto /usr/share/texmf-dist/fonts/enc/dvips/roboto
COPY --from=fonts /usr/share/texmf-dist/fonts/enc/dvips/sourcesanspro /usr/share/texmf-dist/fonts/enc/dvips/sourcesanspro
COPY --from=fonts /usr/share/texmf-dist/fonts/map/dvips/fontawesome5 /usr/share/texmf-dist/fonts/map/dvips/fontawesome5
COPY --from=fonts /usr/share/texmf-dist/fonts/map/dvips/roboto /usr/share/texmf-dist/fonts/map/dvips/roboto
COPY --from=fonts /usr/share/texmf-dist/fonts/map/dvips/sourcesanspro /usr/share/texmf-dist/fonts/map/dvips/sourcesanspro
RUN mktexlsr
RUN mkdir -p /var/log/supervisor /var/run && chmod a+w /var/run
RUN mkdir -p /var/cache/nginx/.cache/uv && chown nginx /var/cache/nginx/.cache/uv

COPY --from=builder /cv/dist /usr/share/nginx/html
COPY cgi-bin /usr/share/nginx/cgi-bin
COPY tex /usr/share/nginx/tex
COPY container/nginx.conf /etc/nginx/conf.d/default.conf
COPY container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN uv sync --project=/usr/share/nginx/cgi-bin --frozen
RUN TEST=1 uv run --project=/usr/share/nginx/cgi-bin /usr/share/nginx/cgi-bin/pdf.py --all -o /tmp/resume-selftest.pdf \
	&& rm -f /tmp/resume-selftest.pdf

EXPOSE 80
ENTRYPOINT ["sh", "-c", "rm -f /var/run/fcgiwrap.socket; /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf"]
