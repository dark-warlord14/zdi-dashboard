# ZDI-18-1057: Apple macOS AirPort BrcmNIC Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1057
- **ZDI-CAN:** ZDI-CAN-6150
- **Date:** 2018-09-17
- **CVE:** CVE-2018-4338
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lee @ SECLAB Yonsei University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1057/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the Broadcom Airport kext. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-06-14 - Vulnerability reported to vendor
- 2018-09-17 - Coordinated public release of advisory
- 2018-09-17 - Advisory Updated
