FROM node:lts as dependencies
WORKDIR /fintech-front
COPY package.json package-lock.json ./
RUN npm install --frozen-lockfile

FROM node:lts as builder
WORKDIR /fintech-front
COPY . .
COPY --from=dependencies /fintech-front/node_modules ./node_modules
RUN npm run build

FROM node:lts as runner
WORKDIR /fintech-front
ENV NODE_ENV production
# If you are using a custom next.config.js file, uncomment this line.
COPY --from=builder /fintech-front/next.config.js ./
COPY --from=builder /fintech-front/public ./public
COPY --from=builder /fintech-front/.next ./.next
COPY --from=builder /fintech-front/node_modules ./node_modules
COPY --from=builder /fintech-front/package.json ./package.json

EXPOSE 3000
CMD ["npm", "start"]