FROM node:18-alpine AS builder
WORKDIR /cv
RUN apk add git

# ADD https://github.com/mrozekma/cv.git /cv
COPY . .

RUN yarn install && yarn build

FROM nginx:alpine
#TODO texlive-full is like 3GB. Would be nice to remove it and figure out how to only install the few packages we need.
RUN apk add bash fcgiwrap poetry supervisor texlive texlive-xetex texlive-full uv
RUN mkdir -p /var/log/supervisor /var/run && chmod a+w /var/run
RUN mkdir -p /var/cache/nginx/.cache/uv && chown nginx /var/cache/nginx/.cache/uv

COPY --from=builder /cv/dist /usr/share/nginx/html
COPY cgi-bin /usr/share/nginx/cgi-bin
COPY tex /usr/share/nginx/tex
COPY container/nginx.conf /etc/nginx/conf.d/default.conf
COPY container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN uv sync --project=/usr/share/nginx/cgi-bin --frozen

EXPOSE 80
ENTRYPOINT ["sh", "-c", "rm -f /var/run/fcgiwrap.socket; /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf"]
