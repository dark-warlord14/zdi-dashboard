# ZDI-25-673: Apple Safari getHourCycles Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-673
- **ZDI-CAN:** ZDI-CAN-26616
- **Date:** 2025-07-29
- **CVE:** CVE-2025-43209
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Gary Kwong
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-673/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of getHourCycles API. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/124147

## Disclosure Timeline

- 2025-06-05 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
