# ZDI-20-214: Moxa MGate 5105-MB-EIP DestIP Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-214
- **ZDI-CAN:** ZDI-CAN-9552
- **Date:** 2020-02-11
- **CVE:** CVE-2020-8858
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Moxa
- **Affected Products:** MGate 5105-MB-EIP
- **Credit:** Dove Chiu, Philippe Lin, Charles Perine, Marco Balduzzi, Ryan Flores, Rainer Vosseler
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-214/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Moxa MGate 5105-MB-EIP. Authentication is required to exploit this vulnerability. The specific flaw exists within the DestIP parameter within MainPing.asp. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://www.moxa.com/en/support/support/security-advisory/mgate-5105-mb-eip-series-protocol-gateways-vulnerability

## Disclosure Timeline

- 2019-10-23 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
- 2020-04-01 - Advisory Updated
