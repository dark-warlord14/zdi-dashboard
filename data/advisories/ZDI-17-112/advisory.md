# ZDI-17-112: VIPA Automation WinPLC7 recv Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-112
- **ZDI-CAN:** ZDI-CAN-3721
- **Date:** 2017-02-28
- **CVE:** CVE-2017-5177
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** VIPA
- **Affected Products:** VIPA Automation WinPLC7
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-112/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VIPA Automation WinPLC7. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of TCP packets. The software fails to validate the length field within the packet before copying it to a stack buffer. An attacker can leverage this vulnerability to execute code in the context of the process.

## Additional Details

VIPA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-054-01

## Disclosure Timeline

- 2016-04-28 - Vulnerability reported to vendor
- 2017-02-28 - Coordinated public release of advisory
