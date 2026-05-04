# ZDI-17-645: Fuji Electric Monitouch V-SFT Project File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-645
- **ZDI-CAN:** ZDI-CAN-3994
- **Date:** 2017-08-10
- **CVE:** CVE-2017-9660
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Monitouch V-SFT
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-645/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fuji Electric Monitouch V-SFT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a V8 project file. The issue lies in the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-222-04

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2017-08-10 - Coordinated public release of advisory
