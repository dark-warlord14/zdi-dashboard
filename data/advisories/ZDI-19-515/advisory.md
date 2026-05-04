# ZDI-19-515: Samsung Knox Secure Folder Lock Screen Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-515
- **ZDI-CAN:** ZDI-CAN-7381
- **Date:** 2019-05-29
- **CVE:** CVE-2019-6744
- **CVSS:** 4.3
- **CVSS Vector:** AV:P/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** KNOX
- **Credit:** James dean
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-515/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerability installations of Samsung Secure Folder. An attacker must first obtain physical access to the device in order to exploit this vulnerability. The specific flaws exists within the the handling of the lock screen for Secure Folder. The issue results from the lack of proper validation that a user has correctly authenticated. An attacker can leverage this vulnerability to disclose the contents of the secure container.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/securityUpdate.smsb

## Disclosure Timeline

- 2019-02-01 - Vulnerability reported to vendor
- 2019-05-29 - Coordinated public release of advisory
