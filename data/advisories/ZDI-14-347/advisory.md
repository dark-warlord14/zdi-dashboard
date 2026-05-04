# ZDI-14-347: (0Day) GoPro HERO 3+ gpExec start Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-347
- **ZDI-CAN:** ZDI-CAN-2162
- **Date:** 2014-10-02
- **CVE:** CVE-2014-6433
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** GoPro
- **Affected Products:** HERO 3+
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-347/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GoPro HERO 3+. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gpExec component. This component performs insufficient parameter validation on the a1/a2 parameters when the c1/c2 parameters are set to "start". Successful exploitation will allow an attacker to execute an arbitrary file on the target device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. 03/08/2014 - ZDI reached out to the vendor 03/08/2014 - Vendor sent an automated reply 03/18/2014 - ZDI reached out to the vendor 03/19/2014 - Vendor replied that they are not "interested in such services" 03/24/2014 - ZDI requested escalation with the vendor 03/25/2014 - Vendor reached out to ZDI w/appropriate contact person and PGP 03/26/2014 - ZDI disclosed to the vendor 03/26/2014 - Vendor acknowledged 06/18/2014 - ZDI sent request for update 06/18/2014 - Vendor replied 'no update' 08/25/2014 - ZDI sent request for update/ETA 08/25/2014 - Vendor replied 'no ETA' 09/15/2014 - ZDI sent request for update/ETA -- Vendor Response: GoPro intends to address this Hero 3 Plus issue in the next release for the product, and will update ZDI with a link to the GoPro website at that time.

## Disclosure Timeline

- 2014-03-08 - Vulnerability reported to vendor
- 2014-10-02 - Coordinated public release of advisory
