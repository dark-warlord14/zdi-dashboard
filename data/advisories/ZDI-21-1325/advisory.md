# ZDI-21-1325: Ivanti Avalanche MapShare Service Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1325
- **ZDI-CAN:** ZDI-CAN-15168
- **Date:** 2021-11-19
- **CVE:** CVE-2021-42129
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1325/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the mapShare method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in version Avalanche 6.3.3

## Disclosure Timeline

- 2021-09-22 - Vulnerability reported to vendor
- 2021-11-19 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
