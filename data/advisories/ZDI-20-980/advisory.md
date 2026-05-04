# ZDI-20-980: Canonical Ubuntu Point-to-Point Protocol Daemon Arbitrary File Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-980
- **ZDI-CAN:** ZDI-CAN-11504
- **Date:** 2020-08-11
- **CVE:** CVE-2020-15704
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Thomas Chauchefoin (@swapgs) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-980/
## Vulnerability Details

This vulnerability allows local attackers to read arbitrary files on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of environment variables in pppd. The issue results from the lack of proper validation of user-supplied data, which can allow the read of arbitrary files. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

https://ubuntu.com/security/notices/USN-4451-1 https://ubuntu.com/security/notices/USN-4451-2

## Disclosure Timeline

- 2020-07-22 - Vulnerability reported to vendor
- 2020-08-11 - Coordinated public release of advisory
