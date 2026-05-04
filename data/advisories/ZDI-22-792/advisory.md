# ZDI-22-792: Apple macOS ImageIO WebP File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-792
- **ZDI-CAN:** ZDI-CAN-16158
- **Date:** 2022-05-26
- **CVE:** CVE-2022-26711
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** actae0n of Blacksun Hackers Club
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-792/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of WebP images in the ImageIO framework. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading from memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213257

## Disclosure Timeline

- 2022-02-25 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
