# ZDI-08-079: Trillian AIM Plugin Malformed XML Tag Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-079
- **ZDI-CAN:** ZDI-CAN-410
- **Date:** 2008-12-04
- **CVE:** CVE-2008-5403
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Cerulean Studios
- **Affected Products:** Trillian
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cerulean Studios Trillian. Authentication is not required to exploit this vulnerability. The specific flaw exists within the XML processing code for Trillian. When parsing a malformed XML tag, the application does not allocate enough space for it's contents. During copying of this to the newly allocated buffer, the application will overwrite heap structures with attacker-supplied data that can then be leveraged to achieve code execution with the privileges of the application.

## Additional Details

Cerulean Studios has issued an update to correct this vulnerability. More details can be found at: http://blog.ceruleanstudios.com/?p=404

## Disclosure Timeline

- 2008-11-24 - Vulnerability reported to vendor
- 2008-12-04 - Coordinated public release of advisory
