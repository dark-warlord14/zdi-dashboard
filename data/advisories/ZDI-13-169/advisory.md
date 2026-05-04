# ZDI-13-169: Hewlett-Packard LoadRunner Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-169
- **ZDI-CAN:** ZDI-CAN-1735
- **Date:** 2013-07-26
- **CVE:** CVE-2013-4800
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-169/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of connections using SSL. The issue lies in the failure to validate the length of data before copying it into a fixed-size buffer. An attacker can leverage this vulnerability to gain code execution as SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03862772

## Disclosure Timeline

- 2013-02-15 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
