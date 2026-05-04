# ZDI-21-265: Google Android fts_driver_test_write Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-265
- **ZDI-CAN:** ZDI-CAN-11087
- **Date:** 2021-03-09
- **CVE:** CVE-2021-0460
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** Jesse Chang and Jack Tang of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-265/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Google Android. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the fts_driver_test_write function. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://source.android.com/security/overview/acknowledgements

## Disclosure Timeline

- 2020-05-15 - Vulnerability reported to vendor
- 2021-03-09 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
