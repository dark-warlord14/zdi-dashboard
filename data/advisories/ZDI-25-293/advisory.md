# ZDI-25-293: Microsoft Windows Installer Service Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-293
- **ZDI-CAN:** ZDI-CAN-26153
- **Date:** 2025-05-21
- **CVE:** CVE-2025-29837
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-293/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer service. By creating a symbolic link, an attacker can abuse the service to gain read access to arbitrary files. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user and disclose stored credentials, leading to further compromise.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29837

## Disclosure Timeline

- 2025-01-09 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
