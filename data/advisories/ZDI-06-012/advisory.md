# ZDI-06-012: Sophos Anti-Virus CAB Unpacking Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-012
- **ZDI-CAN:** ZDI-CAN-032
- **Date:** 2006-05-08
- **CVE:** CVE-2006-0994
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sophos
- **Affected Products:** Sophos Anti-Virus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sophos AntiVirus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the unpacking of Microsoft Cabinet files that contain invalid folder count values within the CAB header. Parsing of a specially crafted cabinet file can lead to an exploitable heap corruption. This vulnerability is only exposed when cabinet file inspection is explicitly enabled.

## Additional Details

Sophos has issued an update to correct this vulnerability. More details can be found at: http://www.sophos.com/support/knowledgebase/article/4934.html

## Disclosure Timeline

- 2006-03-20 - Vulnerability reported to vendor
- 2006-05-08 - Coordinated public release of advisory
