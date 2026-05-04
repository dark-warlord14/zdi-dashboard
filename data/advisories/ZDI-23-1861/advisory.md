# ZDI-23-1861: oFono SMS Decoder Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1861
- **ZDI-CAN:** ZDI-CAN-20971
- **Date:** 2023-12-20
- **CVE:** CVE-2023-2794
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** oFono
- **Affected Products:** oFono
- **Credit:** Mitch Zakocs @ ASU SEFCOM Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1861/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of oFono. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of SMS PDUs. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

oFono has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=2255387

## Disclosure Timeline

- 2023-05-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
