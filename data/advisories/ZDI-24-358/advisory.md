# ZDI-24-358: GitLab Label Description Uncontrolled Resource Consumption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-358
- **ZDI-CAN:** ZDI-CAN-21883
- **Date:** 2024-04-01
- **CVE:** CVE-2024-2818
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** GitLab
- **Affected Products:** GitLab
- **Credit:** Quintin Crist of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-358/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of GitLab. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of label descriptions. By sending a crafted request, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

GitLab has issued an update to correct this vulnerability. More details can be found at: https://about.gitlab.com/releases/2024/03/27/security-release-gitlab-16-10-1-released/#DOS%20using%20crafted%20emojis

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2024-04-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
