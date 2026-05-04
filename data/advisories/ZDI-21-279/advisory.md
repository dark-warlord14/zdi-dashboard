# ZDI-21-279: Google Android fts_driver_test_write Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-279
- **ZDI-CAN:** ZDI-CAN-11094
- **Date:** 2021-03-12
- **CVE:** CVE-2021-0457
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Android
- **Credit:** Jesse Chang and Jack Tang of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-279/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Google Android. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the fts_driver_test_write function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://source.android.com/security/overview/acknowledgements

## Disclosure Timeline

- 2020-05-20 - Vulnerability reported to vendor
- 2021-03-12 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
