# ZDI-16-615: Moxa SoftCMS AspWebServer URL Processing Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-615
- **ZDI-CAN:** ZDI-CAN-4032
- **Date:** 2016-11-23
- **CVE:** CVE-2016-8360
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Moxa
- **Affected Products:** SoftCMS
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-615/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa SoftCMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of requests to the web server. A crafted URL can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of Administrator.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-322-02

## Disclosure Timeline

- 2016-10-11 - Vulnerability reported to vendor
- 2016-11-23 - Coordinated public release of advisory
