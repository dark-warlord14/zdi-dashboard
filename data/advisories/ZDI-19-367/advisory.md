# ZDI-19-367: (Pwn2Own) Xiaomi Mi6 Browser CalculateInstanceSizeHelper Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-367
- **ZDI-CAN:** ZDI-CAN-7482
- **Date:** 2019-04-15
- **CVE:** CVE-2018-6065
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-367/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Xiaomi Mi6 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the CalculateInstanceSizeHelper function. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This is resolved with Xiaomi Browser versionName:10.4.0, versionCode:20181211.

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
