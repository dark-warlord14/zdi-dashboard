# ZDI-21-616: GE Reason RPV311 Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-616
- **ZDI-CAN:** ZDI-CAN-11852
- **Date:** 2021-05-27
- **CVE:** CVE-2021-31477
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** GE
- **Affected Products:** Reason RPV311
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-616/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GE Reason RPV311. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware and filesystem of the device. The firmware and filesystem contain hard-coded default credentials. An attacker can leverage this vulnerability to execute code in the context of the download user.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://www.gegridsolutions.com/products/support/GES-2021-005%20-%20RPV311%20Security%20Notice.pdf

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-05-27 - Coordinated public release of advisory
