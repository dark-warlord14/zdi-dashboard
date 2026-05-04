# ZDI-15-407: Apache ActiveMQ RestFilter Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-407
- **ZDI-CAN:** ZDI-CAN-3005
- **Date:** 2015-08-31
- **CVE:** CVE-2015-1830
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apache
- **Affected Products:** ActiveMQ
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-407/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apache ActiveMQ. Authentication is not required to exploit this vulnerability. The specific flaw exists within ActiveMQ fileserver web application. By issuing specially crafted requests, an attacker can create an arbitrary file on the server with attacker controlled data. An attacker can leverage this vulnerability to execute code under the context of the user.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: http://activemq.apache.org/security-advisories.data/CVE-2015-1830-announcement.txt

## Disclosure Timeline

- 2015-06-30 - Vulnerability reported to vendor
- 2015-08-31 - Coordinated public release of advisory
