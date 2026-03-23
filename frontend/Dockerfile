#!/usr/bin/env -S docker build . --tag=m00d-frontend --file

ARG NODE_VERSION="24"

FROM node:${NODE_VERSION}-alpine AS build

RUN npm install --global --force corepack@latest && \
    corepack enable pnpm && \
    corepack use pnpm@latest

WORKDIR /app

COPY . .

RUN --mount=type=cache,target=/.pnpm-store \
    pnpm config set store-dir /.pnpm-store && \
    pnpm config set package-import-method copy && \
    pnpm install --frozen-lockfile --prefer-offline --ignore-scripts && \
    pnpm run build

# -=-

FROM nginx:alpine

LABEL org.opencontainers.image.authors="Chris Post <admin@postfmly.com>" \
    org.opencontainers.image.description="Mood tracker (Frontend)" \
    org.opencontainers.image.licenses="GPL-3.0-only" \
    org.opencontainers.image.title="m00d (Frontend)" \
    org.opencontainers.image.url="https://github.com/chump29/m00d"

# hadolint ignore=DL3018
RUN apk add --no-cache tzdata && \
    rm -rf /usr/share/nginx/html/*

WORKDIR /usr/share/nginx/html

COPY --from=build /app/dist .

COPY nginx.conf /etc/nginx/conf.d/default.conf

ENV TZ=Etc/GMT

HEALTHCHECK --interval=60s CMD ./usr/share/nginx/html/healthcheck.sh

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
