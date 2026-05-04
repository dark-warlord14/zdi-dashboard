# ZDI-08-027: CA BrightStor ARCserve Backup caloggerd Arbitrary File Writing Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-027
- **ZDI-CAN:** ZDI-CAN-088
- **Date:** 2008-05-19
- **CVE:** CVE-2008-2241
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Computer Associates ARCserve Backup. Authentication is not required exploit this vulnerability. The specific flaw exists within the caloggerd log daemon during the processing of log messages that contain directory traversal modifiers. A lack of sanity checking on the provided path allows attackers to append arbitrary data to a file of their choosing and can easily result in a full system compromise.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID=176798

## Disclosure Timeline

- 2006-09-12 - Vulnerability reported to vendor
- 2008-05-19 - Coordinated public release of advisory
