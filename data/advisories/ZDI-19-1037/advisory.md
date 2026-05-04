# ZDI-19-1037: Hewlett Packard Enterprise Intelligent Management Center tftpserver Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1037
- **ZDI-CAN:** ZDI-CAN-8935
- **Date:** 2020-01-29
- **CVE:** CVE-2020-24646
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** Dusan Stevanovic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the val1 parameter provided to the tftpserver component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpsc/doc/public/display?docId=a00093539en_us

## Disclosure Timeline

- 2019-08-07 - Vulnerability reported to vendor
- 2020-01-29 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
