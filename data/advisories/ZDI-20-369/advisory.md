# ZDI-20-369: VMware Workstation OVF NTLM Challenge Response Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-369
- **ZDI-CAN:** ZDI-CAN-9345
- **Date:** 2020-04-03
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Daniel Sese Benjumea and Manuel Fernandez-Aramburu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-369/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Vmware Workstation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of OVF files. By manipulating the OVF file, an attacker can obtain an NTLM challenge response from the current user. An attacker can leverage this vulnerability to impersonate the current user on the network.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://docs.vmware.com/en/VMware-Workstation-Pro/15.5/rn/VMware-Workstation-1552-Pro-Release-Notes.html

## Disclosure Timeline

- 2019-12-10 - Vulnerability reported to vendor
- 2020-04-03 - Coordinated public release of advisory
