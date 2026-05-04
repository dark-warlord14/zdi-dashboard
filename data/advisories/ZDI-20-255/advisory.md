# ZDI-20-255: (Pwn2Own) Samsung Galaxy S10 Call Control Setup Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-255
- **ZDI-CAN:** ZDI-CAN-9658
- **Date:** 2020-02-20
- **CVE:** CVE-2020-8860
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S10
- **Credit:** @fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-255/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy 10. User interaction is required to exploit this vulnerability in that the target must answer a phone call. The specific flaw exists within the Call Control Setup messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the baseband processor.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/securityUpdate.smsb

## Disclosure Timeline

- 2019-11-07 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
- 2020-02-21 - Advisory Updated
