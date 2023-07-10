FROM wettyoss/wetty
RUN apk add python3 py3-pip git nano vim
COPY Flask /Flask
COPY init.sh /init.sh
RUN pip3 install -r /Flask/requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["/bin/sh", "/init.sh"]
