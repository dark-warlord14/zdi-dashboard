# ZDI-06-045: Sophos Anti-Virus CPIO Archive Parsing Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-045
- **ZDI-CAN:** ZDI-CAN-090
- **Date:** 2006-12-12
- **CVE:** CVE-2006-6335
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sophos
- **Affected Products:** Sophos Anti-Virus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sophos Anti-Virus. The specific flaw exists in the parsing of CPIO archives. When a long non-null terminated filename is processed by veex.dll, a stack overflow occurs. Exploitation is possible leading to remote code execution running under the SYSTEM context.

## Additional Details

Sophos has issued an update to correct this vulnerability. More details can be found at: http://www.sophos.com/support/knowledgebase/article/17340.html

## Disclosure Timeline

- 2006-09-14 - Vulnerability reported to vendor
- 2006-12-12 - Coordinated public release of advisory
