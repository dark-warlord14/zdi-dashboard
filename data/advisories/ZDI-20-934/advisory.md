# ZDI-20-934: X.Org Server Pixel Data Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-934
- **ZDI-CAN:** ZDI-CAN-11426
- **Date:** 2020-08-04
- **CVE:** CVE-2020-14347
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** X.Org
- **Affected Products:** Server
- **Credit:** Jan-Niklas Sohn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-934/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of X.Org Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of pixel data. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of root.

## Additional Details

X.Org has issued an update to correct this vulnerability. More details can be found at: https://lists.x.org/archives/xorg-announce/2020-July/003051.html

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-08-04 - Coordinated public release of advisory
