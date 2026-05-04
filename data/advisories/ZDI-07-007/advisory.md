# ZDI-07-007: Hewlett-Packard Mercury LoadRunner Agent Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-007
- **ZDI-CAN:** ZDI-CAN-112
- **Date:** 2007-02-08
- **CVE:** CVE-2007-0446
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mercury Mercury Mercury
- **Affected Products:** Performance Center Monitor over Firewall LoadRunner
- **Credit:** Eric DETOISIEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Mercury LoadRunner Agent, Mercury Performance Center Agent and Mercury Monitor over Firewall. Authentication is not required to exploit this vulnerability. The specific flaw exists within the process magentproc.exe that binds to TCP port 54345. When parsing packets containing an overly long 'server_ip_name' field, an exploitable stack overflow may be triggered due to an an inline strcpy() within the library mchan.dll.

## Additional Details

Mercury has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c00854250

## Disclosure Timeline

- 2006-10-27 - Vulnerability reported to vendor
- 2007-02-08 - Coordinated public release of advisory
