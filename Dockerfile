FROM kaggle/python:latest

# https://github.com/gliderlabs/herokuish/releases/download/v0.3.0/herokuish_0.3.0_linux_x86_64.tgz

RUN curl -L -k https://github.com/gliderlabs/herokuish/releases/download/v0.3.0/herokuish_0.3.0_linux_x86_64.tgz -L |tar -xzC /bin

COPY / /app/

# install herokuish supported buildpacks and entrypoints
RUN /bin/herokuish buildpack install \
	&& ln -s /bin/herokuish /build \
	&& ln -s /bin/herokuish /start \
	&& ln -s /bin/herokuish /exec

