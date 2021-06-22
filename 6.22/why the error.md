hostname, aliases, ipaddrs = gethostbyaddr(name)

원래 코드

hostname, aliases, ipaddrs = gethostbyaddr('')

고친 코드 



hostname에 한글이 있어서 오류가 생기는 것이다.

cmd->hostname 으로 검색하면 hostname에 한글이 없는지 있는지를 알 수 있다.

따라서 hostname을 영어로 바꿨다.

물론 hostname, aliases, ipaddrs = gethostbyaddr(name)으로 다시 고쳤다.

