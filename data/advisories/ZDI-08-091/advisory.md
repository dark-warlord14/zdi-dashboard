# ZDI-08-091: RealNetworks Helix Server NTLM Authentication Malformed Base64 Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-091
- **ZDI-CAN:** ZDI-CAN-380
- **Date:** 2008-12-16
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** Helix Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of RealNetworks Helix Server. Authentication is not required to exploit this vulnerability. The specific flaw exists during NTLM negotiation. The function responsible for decoding Base64 will return a length value on success and 0xFFFFFFFF on failure. The variable used for the return value is unsigned and is interpreted as an actual length value later on. This discrepancy leads to a heap overflow while attempting to copy 0xFFFFFFFF bytes worth of data. Exploitation leads to arbitrary code execution under the context of the SYSTEM user.

## Disclosure Timeline

- 2008-08-19 - Vulnerability reported to vendor
- 2008-12-16 - Coordinated public release of advisory
