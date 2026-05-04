# ZDI-15-442: CODESYS Gateway Server Opcode 0x3f0 Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-442
- **ZDI-CAN:** ZDI-CAN-2786
- **Date:** 2015-09-16
- **CVE:** CVE-2015-6460
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Codesys
- **Affected Products:** Gateway Server
- **Credit:** Josep Pi Rodriguez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-442/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CODESYS Gateway Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the 0x03f0 opcode. An attacker can send a large buffer of data to the server which causes a heap buffer overflow. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Codesys has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-258-02

## Disclosure Timeline

- 2015-03-11 - Vulnerability reported to vendor
- 2015-09-16 - Coordinated public release of advisory
