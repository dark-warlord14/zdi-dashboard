# ZDI-17-348: (Pwn2Own) Apple macOS WindowServer _XGetConnectionPSN Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-348
- **ZDI-CAN:** ZDI-CAN-4599
- **Date:** 2017-05-15
- **CVE:** CVE-2017-2540
- **CVSS:** 1.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-348/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the WindowServer process. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207797

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
