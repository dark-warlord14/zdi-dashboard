# ZDI-13-256: Cisco Data Center Network Manager downloadServlet Remote Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-256
- **ZDI-CAN:** ZDI-CAN-1768
- **Date:** 2013-11-24
- **CVE:** CVE-2013-5487
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-256/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DownloadServlet. Without prior authentication, an attacker could invoke the DownloadServlet to disclose an arbitrary file from the file system. With this information, a remote attacker could abuse this to execute arbitrary code against the target server.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20130918-dcnm

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
