# ZDI-24-420: SonicWALL GMS Virtual Appliance ECMPolicy XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-420
- **ZDI-CAN:** ZDI-CAN-22675
- **Date:** 2024-05-07
- **CVE:** CVE-2024-29010
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** Erik Wynter
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-420/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of SonicWALL GMS Virtual Appliance. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ECMPolicyRequest class. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0007

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-05-07 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
