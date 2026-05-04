# ZDI-13-205: Hewlett-Packard SiteScope SOAP Call runOMAgentCommand Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-205
- **ZDI-CAN:** ZDI-CAN-1678
- **Date:** 2013-08-13
- **CVE:** CVE-2013-2367
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** SiteScope
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-205/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP SiteScope. Authentication is not required to exploit this vulnerability. The specific flaw exists within APIBSMIntegrationImpl's processing of the runOMAgentCommand which can be invoked through SOAP requests without prior authentication. The omHost key can take in a value containing a windows shell command. An attacker can exploit this condition to gain remote code execution as SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03839862

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
