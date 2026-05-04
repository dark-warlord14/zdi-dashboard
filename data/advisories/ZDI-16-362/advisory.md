# ZDI-16-362: Eclipse Jetty Protected Resource Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-362
- **ZDI-CAN:** ZDI-CAN-3707
- **Date:** 2016-06-03
- **CVE:** CVE-2016-4800
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Eclipse
- **Affected Products:** Jetty
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-362/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Eclipse Jetty. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way the ContextHandler class restricts access to protected resources. By issuing a crafted request, an attacker can gain access to the code of a web application deployed in Jetty. An attacker can use this knowledge in further attacks against the web application. Additionally, if the web application allows file uploads, it may be possible for an attacker to modify the code of the web application, achieving a direct path to executing arbitrary code under the context of the server process.

## Additional Details

Eclipse has issued an update to correct this vulnerability. More details can be found at: http://www.ocert.org/advisories/ocert-2016-001.html

## Disclosure Timeline

- 2016-05-03 - Vulnerability reported to vendor
- 2016-06-03 - Coordinated public release of advisory
