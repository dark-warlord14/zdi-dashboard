# ZDI-15-256: (0Day) (Mobile Pwn2Own) Samsung Galaxy S5 MethodSpec Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-256
- **ZDI-CAN:** ZDI-CAN-2613
- **Date:** 2015-06-24
- **CVE:** CVE-2015-4034
- **CVSS:** 7.9
- **CVSS Vector:** AV:A/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S5
- **Credit:** Team MBSD
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-256/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable Samsung Galaxy S5s. Authentication is not required to exploit this vulnerability. The specific flaw exists within the com.absolute.android.persistence.MethodSpec Class. The createFromParcel() method performs dynamic class loading but does not restrict the source of the classes to be loaded. An attacker can craft a Parcelable object specifying arbitrary class files that will be loaded when the MethodSpec object is deserialized, resulting in remote code execution as the system user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/11/2015 - ZDI disclosed this report from Mobile Pwn2Own to the vendor 11/11/2015 - The vendor re-sent ZDI an encryption key 11/11/2015 - ZDI then re-disclosed this report from Mobile Pwn2Own to the vendor 03/13/2015 - ZDI requested a status update 05/13/2015 - ZDI requested a status update 05/18/2015 - ZDI requested a status update -- Vendor Response: Fixes for both issues ZDI-CAN-2613 and ZDI-CAN-2614 require FOTA updates from carriers, such that there is no link to a patch for these fixes. While we believe only a small number of devices haven't received the software (FOTA) update from their respective carriers, there are number of devices still at risk from those vulnerabilities.

## Disclosure Timeline

- 2014-11-13 - Vulnerability reported to vendor
- 2015-06-24 - Coordinated public release of advisory
