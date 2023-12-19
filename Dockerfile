FROM python:3.10

# Add non-root user
ARG USERNAME=nonroot
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME
## Make sure to reflect new user in PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

# Install production and dev dependencies
COPY --chown=nonroot:1000 requirements.txt /tmp/requirements.txt
COPY --chown=nonroot:1000 requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt -r /tmp/requirements-dev.txt && \
    rm /tmp/requirements.txt /tmp/requirements-dev.txt
