# ZDI-14-279: Hewlett-Packard Application Lifecycle Manager DLL Planting Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-279
- **ZDI-CAN:** ZDI-CAN-2138
- **Date:** 2014-08-12
- **CVE:** CVE-2014-2631
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Lifecycle Management
- **Credit:** Dave Weinstein HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard's Application Lifecycle Management. This vulnerability requires the attacker to have an unprivileged account on the Application Lifecycle Management System. The specific flaw exists within the ACLs on a specific installed directory. Because this directory allows any user to create a file, an unprivileged attacker can place a malicious DLL on the system. When the Application Lifecycle Management is restarted, it will execute the provided file in the context of NT Authority\SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04394553

## Disclosure Timeline

- 2014-02-18 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
