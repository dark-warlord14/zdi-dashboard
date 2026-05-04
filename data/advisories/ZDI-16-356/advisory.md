# ZDI-16-356: Apache ActiveMQ Fileserver File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-356
- **ZDI-CAN:** ZDI-CAN-3696
- **Date:** 2016-05-24
- **CVE:** CVE-2016-3088
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apache
- **Affected Products:** ActiveMQ
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-356/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache ActiveMQ. Authentication may or may not be required to exploit this vulnerability, depending on how the product has been configured. The specific flaw exists within the "fileserver" web application. By sending a specially crafted request to the server, an attacker can upload arbitrary code that will be executed the next time the service restarts. An attacker can leverage this vulnerability to execute arbitrary code in the context of the ActiveMQ service.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://activemq.apache.org/security-advisories.data/CVE-2016-3088-announcement.txt

## Disclosure Timeline

- 2016-04-14 - Vulnerability reported to vendor
- 2016-05-24 - Coordinated public release of advisory
