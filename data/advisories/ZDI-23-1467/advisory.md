# ZDI-23-1467: Mozilla Firefox JIT Boolean Conversion Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1467
- **ZDI-CAN:** ZDI-CAN-18594
- **Date:** 2023-09-27
- **CVE:** N/A
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1467/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of boolean conversions in the JIT engine. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.mozilla.org/show_bug.cgi?id=1788528

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
