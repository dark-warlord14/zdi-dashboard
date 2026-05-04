# ZDI-08-030: Trillian Multiple Protocol XML Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-030
- **ZDI-CAN:** ZDI-CAN-311
- **Date:** 2008-05-21
- **CVE:** CVE-2008-2408
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Cerulean Studios
- **Affected Products:** Trillian
- **Credit:** tw33k and n8
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cerulean Studios Trillian Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within XML parsing in talk.dll. When processing certain malformed attributes within an 'IMG' tags, it is possible to overwrite past an allocated heap chunk which can eventually lead to code execution under the context of the currently user.

## Additional Details

Trillian v3.1.10.0 has been released to address these vulnerabilities and is available at http://www.ceruleanstudios.com/downloads/

## Disclosure Timeline

- 2008-04-08 - Vulnerability reported to vendor
- 2008-05-21 - Coordinated public release of advisory
