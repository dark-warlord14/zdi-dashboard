# ZDI-20-215: Apple macOS IO80211Family Stack-based Buffer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-215
- **ZDI-CAN:** ZDI-CAN-9595
- **Date:** 2020-02-11
- **CVE:** CVE-2020-3839
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** s0ngsari @ Theori, Lee @ Seoul National University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-215/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the IO80211Family kernel extension. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210919

## Disclosure Timeline

- 2019-12-17 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
