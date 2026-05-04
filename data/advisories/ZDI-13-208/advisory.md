# ZDI-13-208: Hewlett-Packard LoadRunner Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-208
- **ZDI-CAN:** ZDI-CAN-1734
- **Date:** 2013-08-13
- **CVE:** CVE-2013-4799
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-208/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of XDR. The issue lies in the handling of the length of the XDR-encoded data. The length is not properly validated before being used to allocate a buffer. An attacker can leverage this vulnerability to gain code execution as SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03862772

## Disclosure Timeline

- 2013-02-15 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
