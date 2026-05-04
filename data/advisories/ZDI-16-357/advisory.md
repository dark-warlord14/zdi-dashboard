# ZDI-16-357: Apache ActiveMQ MOVE Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-357
- **ZDI-CAN:** ZDI-CAN-3600
- **Date:** 2016-05-24
- **CVE:** CVE-2016-3088
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apache
- **Affected Products:** ActiveMQ
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-357/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache ActiveMQ. Authentication may or may not be required to exploit this vulnerability, according to how the product has been configured. The specific flaw exists within the fileserver web service that is installed as part of this product. By issuing an HTTP PUT request and an HTTP MOVE request, an attacker can create an arbitrary file on the server with attacker controlled data. An attacker can further leverage this vulnerability to execute code on the server under the context of the ActiveMQ process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://activemq.apache.org/security-advisories.data/CVE-2016-3088-announcement.txt

## Disclosure Timeline

- 2016-03-29 - Vulnerability reported to vendor
- 2016-05-24 - Coordinated public release of advisory
