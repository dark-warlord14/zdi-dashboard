# ZDI-15-111: Cisco Data Center Network Manager FileServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-111
- **ZDI-CAN:** ZDI-CAN-2573
- **Date:** 2015-04-03
- **CVE:** CVE-2015-0666
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-111/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files, and bypass authentication, on a system with vulnerable installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the fmserver servlet which is vulnerable to a directory traversal. An attacker can leverage this vulnerability to read arbitrary files, including operating system files, as the service is installed with SYSTEM privileges by default. An attacker can also bypass webapp authentication because the application writes access tokens to the filesystem, which can be read.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20150401-dcnm

## Disclosure Timeline

- 2014-12-01 - Vulnerability reported to vendor
- 2015-04-03 - Coordinated public release of advisory
