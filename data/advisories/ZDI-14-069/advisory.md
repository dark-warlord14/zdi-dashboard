# ZDI-14-069: Sophos Web Appliance Privilege Escalation and Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-069
- **ZDI-CAN:** ZDI-CAN-2026
- **Date:** 2014-04-08
- **CVE:** CVE-2014-2849
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Sophos
- **Affected Products:** Web Appliance
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-069/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sophos Web Appliance. Authentication is required to exploit this vulnerability. The specific flaws exist within the change_password and netinterface functions of the web appliance. The first flaw will allow for an unprivileged user to change the admin's password and a remote code execution vulnerability exists when updating the network interface. This allows for an attacker to execute under root privileges.

## Additional Details

Sophos has issued an update to correct this vulnerability. More details can be found at: http://www.sophos.com/en-us/support/knowledgebase/120230.aspx

## Disclosure Timeline

- 2014-01-05 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
