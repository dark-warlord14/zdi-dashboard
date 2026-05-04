# ZDI-24-360: JetBrains TeamCity AgentDistributionSettingsController Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-360
- **ZDI-CAN:** ZDI-CAN-23446
- **Date:** 2024-04-01
- **CVE:** CVE-2024-31138
- **CVSS:** 4.6
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** JetBrains
- **Affected Products:** TeamCity
- **Credit:** Alex Williams of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-360/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary script on affected installations of JetBrains TeamCity. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the os parameter provided to the AgentDistributionSettingsController.doPost method. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of arbitrary script. An attacker can leverage this vulnerability to execute script in the context of the current user.

## Additional Details

JetBrains has issued an update to correct this vulnerability. More details can be found at: https://www.jetbrains.com/privacy-security/issues-fixed/

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-04-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
